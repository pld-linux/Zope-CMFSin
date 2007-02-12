%define		zope_subname	CMFSin
Summary:	A Zope product that is a simple syndication client for CMF
Summary(pl.UTF-8):   Dodatek do Zope będący prostym klientem "korporacyjnym" dla CMF
Name:		Zope-%{zope_subname}
Version:	0.6.1
Release:	8
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}.tar.gz
# Source0-md5:	a50ab5b9c13526a6a52397d556b09e84
URL:		http://sourceforge.net/projects/collective/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
Requires:	Zope-CMF
Conflicts:	CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple syndication client for CMF. It uses rssparser and
shares many things in common with CMFNewsFeed but has a different
model for handling channels. It is designed to map _n_ channels or
feeds to sets of composite virtual channels which can then be called
in in a timely fashion.

%description -l pl.UTF-8
CMFSin jest prostym klientem "korporacyjnym" dla CMF. Umożliwia
parsowanie rss i posiada wiele możliwości jakie daje CMFNewsFeed, lecz
różni się innym modelem obsługi kanałów. Jest opracowany tak, by
odwzorowywać _n_ kanałów lub strumieni na zbiory połączonych
wirtualnych kanałów, które mogą być wywoływane o określonej porze.

%prep
%setup -q -n %{zope_subname}

find . -type d -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,skins,www,*.py,*.cfg,*.gif,version.txt,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc docs/* README.txt
%{_datadir}/%{name}
